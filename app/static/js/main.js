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
    if (window.location.pathname === '/') {
        showTab('NewPage');
    }
    if (window.location.pathname === '/setup') {
        showTabSetup('install_start_page')
    }
};

function go_editor(nid) {
    window.location.href = 'http://' + window.location + 'editor?id=' + nid
}

function sendRequestCheck() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
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

function callapi(path) {
    return fetch('http://localhost:65371' + path)
        .then(response => {
            const statusCode = response.status;
            return statusCode;
        });
}

function delete_idea(iid) {
    let confirmed = window.confirm("🥸 你确定要删除这个灵感吗?\n删掉就再也回不来了");
    if (confirmed) {
        callapi('/del/idea?id=' + iid)
            .then(statusCode => {
                if (statusCode == 200) {
                    customElements.get('s-dialog').show('✅ 删除灵感成功\n将在一秒后刷新')
                    setTimeout("location.reload();", 1000)
                } else {
                    customElements.get('s-dialog').show('❎ 请求API失败,请查看后端控制台的输出,状态码:' + statusCode + '\n点击空白处退出')
                }
            });
    }
}

document.getElementById('newidea_record_button').addEventListener('click', function () {
    const title = document.getElementById('newidea_d_title').value.trim();
    const label = document.getElementById('newidea_d_label').value.trim();
    const text = document.getElementById('newidea_d_text').value.trim();
    if (title === "" || label === "" || text === "") {
        customElements.get('s-dialog').show('🤔 都需要填上哦\n点击空白处退出')
        return;
    }
    callapi('/create/idea?title=' + title + "&label=" + label + "&text=" + text)
        .then(statusCode => {
            if (statusCode == 200) {
                customElements.get('s-dialog').show('✅ 记录灵感成功\n将在一秒后刷新')
                setTimeout("location.reload();", 1000)
            } else {
                customElements.get('s-dialog').show('❎ 请求API失败,请查看后端控制台的输出,状态码:' + statusCode + '\n点击空白处退出')
            }
        });
});

$(document).ready(function() {
    $('#waterfall-container').masonry({
        itemSelector: '.card',
        columnWidth: '.card',
        gutter: 20,
        fitWidth: true
    });
});

