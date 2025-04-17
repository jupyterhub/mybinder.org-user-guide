// in sync with list in status.rst
// fixme: can this come from one source?
var fedUrls = [
  'https://2i2c.mybinder.org',
  'https://gesis.mybinder.org',
];

// Use a dictionary to store the rows that should be updated
var urlRows = {};
fedUrls.forEach((url) => {
  document.querySelectorAll("tr").forEach((tr) => {
    if (tr.textContent.includes(url.replace("https://", ""))) {
      urlRows[url] = tr;
    }
  });
});

fedUrls.forEach(async (url) => {
  var urlHealth = url + "/health";
  var urlPrefix = url.split("//")[1].split(".")[0];

  // Query the endpoint and update health icon
  var row = urlRows[url];
  let [
    fieldUrl,
    fieldResponse,
    fieldRegistry,
    fieldHub,
    fieldPods,
    fieldQuota,
  ] = row.querySelectorAll("td");
  try {
    let response = await fetch(urlHealth);
    let resp = await response.json();
    if (resp["ok"] == false) {
      setStatus(fieldResponse, "fail");
    } else {
      setStatus(fieldResponse, "success");
    }

    let [respReg, respHub, respQuota] = resp["checks"];

    if (respReg == false) {
      setStatus(fieldRegistry, "fail");
    } else {
      setStatus(fieldRegistry, "success");
    }

    if (respHub == false) {
      setStatus(fieldHub, "fail");
    } else {
      setStatus(fieldHub, "success");
    }

    fieldPods.textContent = `${respQuota["user_pods"]}/${respQuota["build_pods"]}`;
    fieldQuota.textContent = `${respQuota["quota"]}`;
  } catch (e) {
    setStatus(fieldResponse, "fail");
  }
});

var setStatus = (td, kind) => {
  if (kind == "success") {
    td.textContent = "Success";
    td.style.color = "green";
  } else {
    td.textContent = "Fail";
    td.style.color = "red";
  }
};
