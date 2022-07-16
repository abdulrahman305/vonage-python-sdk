class Verify:
    auth_type = 'params'

    def __init__(self, client):
        self._client = client

    def start_verification(self, params=None, **kwargs):
        return self._client.post(
            self._client.api_host(), "/verify/json", params or kwargs
        )

    def check(self, request_id, params=None, **kwargs):
        return self._client.post(
            self._client.api_host(),
            "/verify/check/json",
            dict(params or kwargs, request_id=request_id),
        )

    def search(self, request_id):
        return self._client.get(
            self._client.api_host(), "/verify/search/json", {"request_id": request_id}, auth_type=Verify.auth_type
        )

    def cancel(self, request_id):
        return self._client.post(
            self._client.api_host(),
            "/verify/control/json",
            {"request_id": request_id, "cmd": "cancel"},
        )

    def trigger_next_event(self, request_id):
        return self._client.post(
            self._client.api_host(),
            "/verify/control/json",
            {"request_id": request_id, "cmd": "trigger_next_event"},
        )

    def psd2(self, params=None, **kwargs):
        return self._client.post(
            self._client.api_host(), "/verify/psd2/json", params or kwargs
        )

