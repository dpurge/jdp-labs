{
    new(title, uid):: {
        "schemaVersion": 39,
        "time": {
            "from": "now-6h",
            "to": "now"
        },
        "timezone": "utc",
        title: title,
        [if uid != '' then 'uid']: uid
    }
}