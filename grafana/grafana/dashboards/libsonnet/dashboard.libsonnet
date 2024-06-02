{
    new(title, uid):: {
        "annotations": {
            "list": []
        },
        "editable": true,
        "fiscalYearStartMonth": 0,
        "graphTooltip": 0,
        "id": 1,
        "links": [],
        "liveNow": false,
        "panels": [],
        "refresh": "",
        "schemaVersion": 39,
        "tags": [],
        "templating": {
            "list": []
        },
        "time": {
            "from": "now-6h",
            "to": "now"
        },
        "timepicker": {},
        "timezone": "utc",
        "title": title,
        [if uid != '' then 'uid']: uid,
        "version": 1,
        "weekStart": ""
    }
}