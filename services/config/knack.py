# Yes, knackpy.App handles TZ settings automatically by fetching it from metadata
# but some scripts may use the lower-level knackpy.api functions, which do not access
# app metadata, but *do* need to query Knack by date, and thus need to know the app's
# timezone. You'll probably never need to change this setting.
APP_TIMEZONE = "US/Central"

CONFIG = {
    "data-tracker": {
        "view_197": {
            "description": "Signals data pub view",
            "scene": "scene_73",
            "modified_date_field": "field_205",
            "socrata_resource_id": "p53x-x73x",
            "location_field_id": "field_182",
            "service_id": "e6eb94d1e7cc45c2ac452af6ae6aa534",
            "item_type": "layer",
            "layer_id": 0,
        },
        "view_395": {
            "description": "CCTV Cameras",
            "scene": "scene_144",
            "modified_date_field": "field_714",
            "socrata_resource_id": "b4k4-adkb",
            "location_field_id": "field_182",
            "service_id": "52f2b5e51b9a4b5e918b0be5646f27b2",
            "layer_id": 0,
            "item_type": "layer",
        },
        "view_2681": {
            "description": "MMC activities",
            "scene": "scene_1075",
            "modified_date_field": "field_2563",
            "socrata_resource_id": "p7pt-re4k",
        },
        "view_2892": {
            "description": "MMC issues",
            "scene": "scene_514",
            "modified_date_field": "field_1385",
            "socrata_resource_id": "v7vh-gbi6",
            "location_field_id": "field_182",
        },
        "view_2863": {
            "description": "Inventory items",
            "scene": "scene_1170",
            "modified_date_field": "field_1229",
        },
        "view_2908": {
            "description": "Metrobike kiosks",
            "scene": "scene_514",
            "modified_date_field": "field_3798",
            "service_id": "7d4d0b1369504383a42b943bd9c03f9a",
            "layer_id": 0,
            "item_type": "layer",
            "location_field_id": "field_3818",
            "socrata_resource_id": "qd73-bsdg",
        },
        "view_1564": {
            "description": "Digital Messaging Signs",
            "scene": "scene_569",
            "modified_date_field": "field_1658",
            "service_id": "e7104494593d4a44a2529e4044ef7d5d",
            "socrata_resource_id": "4r2j-b4rx",
            "location_field_id": "field_182",
            "layer_id": 0,
            "item_type": "layer",
        },
        "view_1829": {
            "description": "Work Orders Signals",
            "scene": "scene_683",
            "modified_date_field": "field_1074",
            "socrata_resource_id": "hst3-hxcz",
            "location_field_id": "field_182",
        },
        "view_1563": {
            "description": "Flashing Beacons",
            "scene": "scene_568",
            "modified_date_field": "field_1701",
            "socrata_resource_id": "wczq-5cer",
            "location_field_id": "field_182",
            "service_id": "6c4392540b684d598c72e52206d774be",
            "layer_id": 0,
            "item_type": "layer",
        },
        "view_1333": {
            "description": "Detectors",
            "scene": "scene_468",
            "modified_date_field": "field_1533",
            "socrata_resource_id": "qpuw-8eeb",
            "location_field_id": "field_182",
            "service_id": "47d17ff3ce664849a16b9974979cd12e",
            "layer_id": 0,
            "item_type": "layer",
        },
        "view_540": {
            "description": "Travel Sensors",
            "scene": "scene_188",
            "modified_date_field": "field_710",
            "socrata_resource_id": "6yd9-yz29",
            "location_field_id": "field_182",
            "service_id": "9776d3e894a74521a7f63443f7becc7c",
            "layer_id": 0,
            "item_type": "layer"
        },
        "view_1063": {
            "description": "Signal Retiming",
            "scene": "scene_375",
            "modified_date_field": "field_1257",
            "socrata_resource_id": "g8w2-8uap",
        },
        "view_1597": {
            "description": "Pole Attachments",
            "scene": "scene_589",
            "modified_date_field": "field_1813",
            "socrata_resource_id": "btg5-ebcy",
            "location_field_id": "field_182",
            "service_id": "3a5a777f780447db940534b5808d4ba7",
            "layer_id": 0,
            "item_type": "layer"
        },
        "view_1201": {
            "description": "Arterial Management Locations",
            "scene": "scene_425",
            "modified_date_field": "field_508",
            "location_field_id": "field_182",
            "service_id": "66f4b5b0339d4275b64f265dd59727e5",
            "layer_id": 0,
            "item_type": "layer"
        },
        "view_1567": {
            "description": "Signal Cabinets",
            "scene": "scene_571",
            "modified_date_field": "field_1793",
            "socrata_resource_id": "x23u-shve",
            "location_field_id": "field_1878",
            "service_id": "c3fd3bb177cc4291880bbe8c630ed5c4",
            "layer_id": 0,
            "item_type": "layer"
        }
    },
    "signs-markings": {
        "view_3099": {
            "description": "Markings work orders",
            "scene": "scene_1249",
            "modified_date_field": "field_2150",
            "service_id": "a9f5be763a67442a98f684935d15729b",
            "layer_id": 1,
            "item_type": "layer",
            "location_field_id": None,
            "socrata_resource_id": "nyhn-669r",
        },
        "view_3100": {
            "description": "Markings jobs",
            "scene": "scene_1249",
            "modified_date_field": "field_2196",
            "service_id": "a9f5be763a67442a98f684935d15729b",
            "layer_id": 0,
            "item_type": "layer",
            "location_field_id": None,
            "socrata_resource_id": "vey3-7n3x",
        },
        "view_3096": {
            "description": "Markings work order attachments",
            "scene": "scene_1249",
            "modified_date_field": "field_2407",
            "service_id": "a9f5be763a67442a98f684935d15729b",
            "layer_id": 0,
            "item_type": "table",
            "location_field_id": None,
        },
        "view_3103": {
            "description": "Markings asset specification actuals",
            "scene": "scene_1249",
            "modified_date_field": "field_3365",
            "service_id": "a9f5be763a67442a98f684935d15729b",
            "layer_id": 1,
            "item_type": "table",
            "location_field_id": None,
        },
        "view_3104": {
            "description": "Markings job materials",
            "scene": "scene_1249",
            "modified_date_field": "field_771",
            "service_id": "a9f5be763a67442a98f684935d15729b",
            "layer_id": 2,
            "item_type": "table",
            "location_field_id": None,
        },
        "view_3106": {
            "description": "Signs asset specification actuals",
            "scene": "scene_1249",
            "modified_date_field": "field_3365",
            "service_id": "93e29b23c39b4110ab0bbefde79b4063",
            "layer_id": 0,
            "item_type": "layer",
            "location_field_id": "field_3300",
        },
        "view_3107": {
            "description": "Signs work orders",
            "scene": "scene_1249",
            "modified_date_field": "field_3206",
            "service_id": "93e29b23c39b4110ab0bbefde79b4063",
            "layer_id": 1,
            "item_type": "layer",
            "location_field_id": "field_3300",
            "socrata_resource_id": "ivss-na93",
        },
        "view_3126": {
            "description": "Signs work order materials",
            "scene": "scene_1249",
            "modified_date_field": "field_771",
            "service_id": "93e29b23c39b4110ab0bbefde79b4063",
            "layer_id": 1,
            "item_type": "table",
        },
        "view_3127": {
            "description": "Signs work order attachments",
            "scene": "scene_1249",
            "modified_date_field": "object_153",
            "service_id": "93e29b23c39b4110ab0bbefde79b4063",
            "item_type": "table",
            "layer_id": 0,
        },
       # Note that views 3307 and 3528 push to the same socrata dataset. This object is a child to
        # both work_orders_markings and work_orders_signs - which share duplicate field names, notably
        # ATD_WORK_ORDER_ID, WORK_TYPE, and LOCATION_NAME. So we source the reimbursements from two
        # similar views, one with connection fields added from markings and the other with fields
        # added from signs. They map one set of columns in Socrata, which matches on the knack field
        # name rather than key.
        "view_3307": {
            "description": "Work Order Markings Time Logs",
            "scene": "scene_1249",
            "modified_date_field": "field_2559",
            "socrata_resource_id": "qvth-gwdv",
        },
        "view_3528": {
            "description": "Work Order Signs Time Logs",
            "scene": "scene_1249",
            "modified_date_field": "field_2559",
            "socrata_resource_id": "qvth-gwdv",
        },
        # Note that views 3526 and 3527 push to the same socrata dataset (see note above). Also
        # that they do not have a "modified_date_field". As a result all records will always be
        # processed. OK in this case since they accumulate at ~500/year.
        "view_3526": {
            "description": "Signs reimburesement tracking",
            "scene": "scene_1249",
            "socrata_resource_id": "pma8-yy5k",
        },
        "view_3527": {
            "description": "Markings reimburesement tracking",
            "scene": "scene_1249",
            "socrata_resource_id": "pma8-yy5k",
        },
    },
    "finance-purchasing": {
        "view_788": {
            "description": "Inventory items",
            "scene": "scene_84",
            "modified_date_field": "field_374",
            "dest_apps": {
                "data-tracker": {
                    "container": "view_2863",
                    "description": "Inventory items",
                    "modified_date_field": "field_1229",
                    "object": "object_15",
                },
            },
        },
    },
}
