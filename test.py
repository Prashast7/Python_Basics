test_dict = {
    "IDOC": {
        "ORDERS": {
            "ORDERNUMBER": "101",
            "POL": "IND",
            "POD": [
                {
                    "QUAL": "001",
                    "Destination": "DE"
                },
                {
                    "QUAL": "002",
                    "Destination": "TEST"
                }
            ]
        }
    }
}

test_config = {
    "orderNumber": {
        "path": "IDOC.ORDERS.ORDERNUMBER"
    },
    "pol": {
        "path": "IDOC.ORDERS.POL"
    },
    "pod": {
        "path": "IDOC.ORDERS.POD",
        "qualifier": {
            "qualifier_field": "QUAL",
            "qualifier_value": "001",
            "field_to_extract": "Destination"
        }
    }
}


def fetch_path(test_dict,test_config):
    x = test_dict[IDOC][ORDERS][ORDERNUMBER]
    y = test_dict[IDOC][ORDERS][POL]





OUTPUT
{
    "orderNumber": "101",
    "pol": "IND",
    "pod": "DE"
}
