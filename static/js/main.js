var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        status: {},
        statusXHR: null,
        log: "",
        logXHR: null,
        logEl: null,
        autoScroll: true
    },
    mounted: function () {
        // status
        this.getStatus();
        setInterval(this.getStatus, 5000);

        // log
        this.logEl = document.getElementById("log");
        this.logXHR = new XMLHttpRequest();
        this.logXHR.open('GET', '/log');
        this.logXHR.send();

        // event listener
        this.logXHR.addEventListener("progress", this.updateLog);
    },
    updated: function () {
        if (this.autoScroll) this.scrollToBottom();
    },
    watch: {
        autoScroll: function(value) {
            if(value) this.scrollToBottom();
        }
    },
    methods: {
        updateLog(e) {
            this.log = e.target.response;
        },
        scrollToBottom() {
            this.logEl.scrollTop = this.logEl.scrollHeight - this.logEl.clientHeight;
        },
        getStatus() {
            fetch("/status")
                .then(response => response.json())
                .then(response => {
                    this.status = response;
                })
                .catch(error => console.error(error));
        },
        start() {
            fetch("/start")
                .then(response => response.json())
                .then(
                    this.getStatus()
                )
                .catch(error => console.error(error));
        },
        stop() {
            if (!confirm("Sicher?")) return;

            fetch("/stop")
                .then(response => response.json())
                .then(
                    this.getStatus()
                )
                .catch(error => console.error(error));
        },
        restart() {
            if (!confirm("Sicher?")) return;

            fetch("/restart")
                .then(response => response.json())
                .then(
                    this.getStatus()
                )
                .catch(error => console.error(error));
        }
    }
});
