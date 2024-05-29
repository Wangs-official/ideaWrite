function showTab(tabId) {
    var tabs = document.getElementsByClassName('view_tab');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].style.display = 'none';
    }
    var selectedTab = document.getElementById(tabId);
    if (selectedTab) {
        selectedTab.style.display = 'block';
        selectedTab.classList.add('active');
    }
    customElements.get('s-snackbar').show('已打开页面: ' + tabId)
}

function showTabSetup(tabId) {
    var tabs = document.getElementsByClassName('view_setup_tab');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].style.display = 'none';
    }
    var selectedTab = document.getElementById(tabId);
    if (selectedTab) {
        selectedTab.style.display = 'block';
    }
}

window.onload = function () {
    if (window.location.pathname === '/'){
        showTab('NewPage');
    }
    if (window.location.pathname === '/setup'){
        showTabSetup('install_start_page')
    }
};

function go_editor(nid){
    window.location.href='http://'+window.location+'editor?id='+nid
}

function sendRequestCheck() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (xhttp.readyState === 4) {
        if (xhttp.status !== 200) {
          var warningElement = document.querySelector(".no_connect_warning");
          warningElement.style.display = "block";
        } else {
          var warningElement = document.querySelector(".no_connect_warning");
          warningElement.style.display = "none";
        }
      }
    };
    xhttp.open("GET", "http://localhost:65371", true);
    xhttp.send();
  }
  setInterval(sendRequestCheck, 1000);
  