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
    print(points_get_data_lambda({'access_token': 'eyJraWQiOiJlMmlkWGpmVUs5SnpFd0U0dElHaG9SMzZEOWc0VVwvaUlMZU5ON0d1eE81OD0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIyMjk5NGI3YS1hMTE3LTQxOTItOWU3Yy00NDFlMjJkYjUxNTgiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfb1llQ1hzdjVFIiwiZXhwIjoxNTEwMDc5NjUzLCJpYXQiOjE1MTAwNzYwNTMsImp0aSI6Ijg0NDU5NDVjLTEzZGYtNDUxMC1iYjA2LTdjZmQ4NWJmYjBjNSIsImNsaWVudF9pZCI6IjNnbGtjZXFncXU4bGVqODJvb2doMnJqMWNkIiwidXNlcm5hbWUiOiJrcmVvZG9udCJ9.WBCVb4MVUgvxvJ9UjtBXuwZny3Z7TpZyIbEHQOFd9qA1pE13aRazYEkWFLz07s80fhgxNJqzdfRb_JUH0kKAmrfkLVXDQ4mmxBn6w8uw_iByOKKMoKh6ae_5dK_t5_4aTjTFNr0X8Bugr2-QXRQxj0n6Y5_YAICh3Cgk7q9ccyZ31Qkm_uK3RfTEu9pSjSNv5F21RA32ZSEYQnWPeOec5xnyJw1HOEPMRTQkqSLY78BEFr018uIG0VTwryJ5TUhjDEUhmoaZLwf9N4eh4Thl2t7uW4xLUCOVXxURl_i7zzYg7myvSR_GRRyiGUxsQvv4iOF-QuLZ1AvGOfGR7TdecA',
                                  'id_token': 'eyJraWQiOiJVblJ3cGlYb2FDUG54QUtnTHZRcEFXSnJwMjhrTjQwRWJQUlpuelwvMmRkYz0iLCJhbGciOiJSUzI1NiJ9.eyJjb2duaXRvOnJvbGVzIjpbImFybjphd3M6aWFtOjo3MDQ0MDAyMzY0ODM6cm9sZVwvbGFtYmRhX2Jhc2ljX2V4ZWN1dGlvbiJdLCJzdWIiOiIyMjk5NGI3YS1hMTE3LTQxOTItOWU3Yy00NDFlMjJkYjUxNTgiLCJhdWQiOiIzZ2xrY2VxZ3F1OGxlajgyb29naDJyajFjZCIsImNvZ25pdG86Z3JvdXBzIjpbImFkbWlucyIsInN1cGVyLWFkbWluIl0sInRva2VuX3VzZSI6ImlkIiwiY29nbml0bzpwcmVmZXJyZWRfcm9sZSI6ImFybjphd3M6aWFtOjo3MDQ0MDAyMzY0ODM6cm9sZVwvbGFtYmRhX2Jhc2ljX2V4ZWN1dGlvbiIsImF1dGhfdGltZSI6MTUxMDA3NjA1MywiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfb1llQ1hzdjVFIiwibmlja25hbWUiOiJLcmVvZG9udCIsImNvZ25pdG86dXNlcm5hbWUiOiJrcmVvZG9udCIsImV4cCI6MTUxMDA3OTY1MywiaWF0IjoxNTEwMDc2MDUzfQ.VVi3E3y_79LT6cLKiHJWrPtJ2rHAbpV-95pb3HeciUfgOudv-uy-hHfjvqip5yX3Azj6Jdr424cbHXm_-jzKQ27ishZBZbCwBV4PELIhi4KLOq6IxzcfrG2C7eLMVAFbAL5dcx7FVhZgwNTIGKBw56VIwr6JJQun8te_oR20_SotvuU4czWB18PAmXxtKt-1WcY8QjdkJIF1hMAnKY2hKs_VfNVwG5bRbnxgZOY-PG7Uqf9Vug-Ucd9MlMJWMwXvYv62HoTROHjTUp-fPzd4tefa12QeoH7_kr17JGQZSeQxiuHhOdq3JUVEqIHu4lZs168haZO3sRoAJIlKZhFBRw'}, {}))