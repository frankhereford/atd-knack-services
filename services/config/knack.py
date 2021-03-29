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
            "dest_apps": {
                "vza": {
                    "container": "view_567",
                    "description": "Signal locations",
                    "modified_date_field": "field_647",
                    "object": "object_41",
                },
            },
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
            # check to see if we need the location_field
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
        },
        "view_3100": {
            "description": "Markings jobs",
            "scene": "scene_1249",
            "modified_date_field": "field_2196",
            "service_id": "a9f5be763a67442a98f684935d15729b",
            "layer_id": 0,
            "item_type": "layer",
            "location_field_id": None,
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
    "vza": {
        "view_567": {
            "description": "Vision Zero in Action (VZA) signal locations",
            "scene": "scene_259",
            "modified_date_field": "field_647",
        },
    },
}
