local dashboard = import 'dashboard.libsonnet';

dashboard.new('Lab 1 pannel example', 'a538aeff-5a8a-42a5-901c-938d896fdd6f') {
    "annotations": {
        "list": [
            {
                "builtIn": 1,
                "datasource": {
                "type": "grafana",
                "uid": "-- Grafana --"
                },
                "enable": true,
                "hide": true,
                "iconColor": "rgba(0, 211, 255, 1)",
                "name": "Annotations & Alerts",
                "type": "dashboard"
            }
        ]
    },
    panels: [
        {
            "datasource": {
                "type": "grafana",
                "uid": "grafana"
            },
            "gridPos": {
                "h": 8,
                "w": 12,
                "x": 0,
                "y": 0
            },
            "id": 1,
            "options": {
                "seriesCountSize": "sm",
                "showSeriesCount": false,
                "text": "Default value of text input option"
            },
            "targets": [
                {
                "datasource": {
                    "type": "datasource",
                    "uid": "grafana"
                },
                "queryType": "randomWalk",
                "refId": "A"
                }
            ],
            "title": "Panel Title",
            "type": "dpurge-lab1-panel"
        },

        {
            "datasource": {
                "type": "grafana-testdata-datasource",
                "uid": "trlxrdZVk"
            },
            "gridPos": {
                "h": 8,
                "w": 12,
                "x": 12,
                "y": 0
            },
            "id": 2,
            "options": {
                "seriesCountSize": "sm",
                "showSeriesCount": false,
                "text": "Default value of text input option"
            },
            "targets": [
                {
                "alias": "",
                "datasource": {
                    "type": "grafana-testdata-datasource",
                    "uid": "db84e60d-b92a-4089-82cb-34842fb1754b"
                },
                "refId": "A",
                "scenarioId": "no_data_points"
                }
            ],
            "title": "Panel Title",
            "type": "dpurge-lab1-panel"
        }
    ]
}
