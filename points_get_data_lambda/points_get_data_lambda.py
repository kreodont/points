import boto3
import base64
import json

cognito_identity_service_provider_client = boto3.client('cognito-idp')


def parse_jwt(jwt_string):
    try:
        def maybe_pad(s):
            return s + '=' * (4 - len(s) % 4)
        jwt_string = jwt_string.replace('"', '').strip()
        header, payload, signature = jwt_string.split(".")
        payload_string = base64.urlsafe_b64decode(maybe_pad(payload)).decode('utf-8')
        payload_json = json.loads(payload_string)
        return payload_json
    except Exception as e:
        return {'result': 'Wrong credentials: %s' % e}


def points_get_data_lambda(event, content):
    if not isinstance(event, dict):
        return {'result': 'Failed'}

    if 'access_token' not in event.keys():
        return {'result': 'Failed'}

    admin_mode = False
    if 'id_token' in event.keys():
        user_details = parse_jwt(event['id_token'])
        if 'cognito:groups' in user_details.keys():
            user_groups = user_details['cognito:groups']
            for group in user_groups:
                if group == 'admins':
                    admin_mode = True
                if group == 'super-admin':
                    admin_mode = True
    access_token = event['access_token']
    try:
        cognito_user = cognito_identity_service_provider_client.get_user(AccessToken=access_token)
    except Exception as e:
        return str(e)

    if not cognito_user:
        return {'result': 'Authentication Failed'}

    return cognito_user

if __name__ == '__main__':
    print(points_get_data_lambda({'access_token': 'eyJraWQiOiJlMmlkWGpmVUs5SnpFd0U0dElHaG9SMzZEOWc0VVwvaUlMZU5ON0d1eE81OD0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIyMjk5NGI3YS1hMTE3LTQxOTItOWU3Yy00NDFlMjJkYjUxNTgiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfb1llQ1hzdjVFIiwiZXhwIjoxNTA5OTg0MDQzLCJpYXQiOjE1MDk5ODA0NDMsImp0aSI6IjQzYTBjM2E5LTAxMGUtNGE0ZC1hYTU2LWZlODI4MmVhZDQzMSIsImNsaWVudF9pZCI6IjNnbGtjZXFncXU4bGVqODJvb2doMnJqMWNkIiwidXNlcm5hbWUiOiJrcmVvZG9udCJ9.kozUCKjGji0xdKBaIbUcIFoeRtriTyOJopTKUWz0HeWP47dRapVJbJRcb1xBJdAszPsJRFElNNB3aWERD7Cu_a6gQKjZQ9oTSBjn-4rof-je1sJWlsfZGytBbqjk0L7vOgaSObwTSmCKO04X-vJDfBqMoGVeTXykl_EBvEuzBQl_GlULcrFZntVsB0yrtccBFkvUMFhKvw_H-OlTMGehLU8mj4GAWcnPc2R6mYiOoc1YkzgYb0_uvFhR98_B7HlbZ17sHA20RRX-CknUnFgUPNnMwu_cOltrfG4n8cg1Sl7AoJPWZUudlRxpgzAYWG5-9otv-xD0_TAi-cKzbYS6Bg',
                                  'id_token': 'eyJraWQiOiJVblJ3cGlYb2FDUG54QUtnTHZRcEFXSnJwMjhrTjQwRWJQUlpuelwvMmRkYz0iLCJhbGciOiJSUzI1NiJ9.eyJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo3MDQ0MDAyMzY0ODM6cm9sZVwvbGFtYmRhX2Jhc2ljX2V4ZWN1dGlvbiJdLCJzdWIiOiIyMjk5NGI3YS1hMTE3LTQxOTItOWU3Yy00NDFlMjJkYjUxNTgiLCJhdWQiOiIzZ2xrY2VxZ3F1OGxlajgyb29naDJyajFjZCIsImNvZ25pdG86Z3JvdXBzIjpbImFkbWlucyIsInN1cGVyLWFkbWluIl0sInRva2VuX3VzZSI6ImlkIiwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo3MDQ0MDAyMzY0ODM6cm9sZVwvbGFtYmRhX2Jhc2ljX2V4ZWN1dGlvbiIsImF1dGhfdGltZSI6MTUwOTk4MDkzMiwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfb1llQ1hzdjVFIiwibmlja25hbWUiOiJLcmVvZG9udCIsImNvZ25pdG86dXNlcm5hbWUiOiJrcmVvZG9udCIsImV4cCI6MTUwOTk4NDUzMiwiaWF0IjoxNTA5OTgwOTMyfQ.bWs-t6EH4rC-b1M0p01YMB3pPSYHzk-53Soewoq-ulA8jRa-UubI9u3sPxTY7Y9RwURZ6nCDQ8X0fdTdXr5m9EGyoQy8ZTR9tS-sW33ewzbNtw7uDB0-9pP6VvpC9cCgon6SI9MEXH2rggC3WPh3iRDE3STR8oTn9KPQ52OhY8xYotEh3MSFQlPVeRLmgioev676mzTX0asxsPy8ScjZ_B-m9M5qj99HMSLCjFLo4ADldRK_0XMhMwSge7es1E21CcqI23mS5u_52DOwQdx3CzOw2XYnjmE_bVEH3j0-8kUJN0RvM_I5IpUE9yIoyeR21GPCy3TLAGOmXVha1Ghq0A'}, {}))