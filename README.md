# example-kiali-redirect

### Steps to Reproduce

1. Install kiali server via the upstream helm chart with `--set server.web_root=/some/random/path/` to change where kiali is served from. Note, this is `/kiali` by default :
https://kiali.io/docs/installation/quick-start/#install-via-helm

2. Follow steps to access the UI:
https://kiali.io/docs/installation/quick-start/#access-to-the-ui

3. Ensure you have the latest Python 3 installation

4. In the root of the example-kiali-redirect, run `python kialiProxy.py`. This will start a passthrough proxy to simulate serving kiali from a proxy.

5. Then navigate to `http://localhost:9097/http://localhost:20001` to access kiali.

6. Once the webpage loads, you will notice that the url is no longer what you navigated to originally `http://localhost:9097/http://localhost:20001`, but the `web_root` has re-written the path portion of the url so that it is `http://localhost:9097/some/random/path/console/overview?duration=60&refresh=15000`. This is a problem because my proxy endpoint is `http://localhost:9097/http://localhost:20001` and additional requests will no longer be hitting the proxy endpoint if the `web_root` rewrites it to `http://localhost:9097/some/random/path/console/overview?duration=60&refresh=15000`
