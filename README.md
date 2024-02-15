# newrelic-service-broker-tile-generator
<b>newrelic-service-broker-tile-generator</b> contains automation to install required dependencies to create a [newrelic-service-broker-tile](https://github.com/newrelic/newrelic-service-broker-tile). config.yaml takes the input params java version, maven version and licence string to replace in the [THIRD_PARTY_NOTICES](https://github.com/newrelic/newrelic-service-broker-tile/blob/master/THIRD_PARTY_NOTICES.md).

## How to use

### Installation
1. Install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```

### Usage
1. Run the Python script:
    ```
    python __init__.py
    ```
