import boto3
import datetime

items_dict = {}

dynamo = boto3.resource('dynamodb')
source_table =  dynamo.Table('points')
response = source_table.scan()
for item in response['Items']:
    if item['points_owner'] not in items_dict.keys():
        items_dict[item['points_owner']] = {}
    if '.' in item['name_date']:
        event_datetime = datetime.datetime.strptime(item['name_date'].split('_')[1], '%Y-%m-%d %H:%M:%S.%f')
    else:
        event_datetime = datetime.datetime.strptime(item['name_date'].split('_')[1], '%Y-%m-%d %H:%M:%S')
    items_dict[item['points_owner']][event_datetime] = item
for points_owner in items_dict.keys():
    cummulative_points = 0
    for key in sorted(items_dict[points_owner].keys()):
        points = int(items_dict[points_owner][key]['points'])
        cummulative_points += points
        print('%s %s %s %s' % (items_dict[points_owner][key]['name_date'], points, cummulative_points, items_dict[points_owner][key]['description']))
    print(points_owner)
    print(cummulative_points)