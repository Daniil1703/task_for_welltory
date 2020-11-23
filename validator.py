import os
import json
import fastjsonschema


directory_jsn = './event/'
directory_sch = './schema/'

files_json = os.listdir(directory_jsn)
files_schema = os.listdir(directory_sch)

def get_schema(file_schema, i):
    fileschema = f"{directory_sch}{files_schema[i]}"
    print(files_schema[i])
    with open(fileschema) as file_schm:
        schema = json.load(file_schm)
    return schema



def get_json(file_json, k):
    filename = f"{directory_jsn}{file_json[k]}"
    print(file_json[k])
    with open(filename) as file_json:
        jsonData = json.load(file_json)
    return jsonData

i = 0
k = 0
count = 0
file_log = open('log.txt', 'w')
readme = open('README.md', 'w')

for k in range(len(files_json)):
    for i in range(len(files_schema)):
        print('data: ', end='')
        jsonData = get_json(files_json, k)
        file_log.write('data: ' + files_json[k] + '\n')
        readme.write('**Data:** ' + files_json[k] + '\n'*2)
        print('schema: ', end='')
        schema = get_schema(files_schema, i)
        file_log.write('schema: ' + files_schema[i] + '\n')
        readme.write('**Schema:** ' + files_schema[i] + '\n'*2)
        try:
            fastjsonschema.validate(schema, jsonData)
        except fastjsonschema.exceptions.JsonSchemaException as err:
            print('error:', err, '\n')
            file_log.write('error: ' + str(err) + '\n'*3)
            readme.write('**error:** ' + str(err) + '\n'*2 + '___' + '\n'*3)
            count += 1

readme.write('## Total errors in files: ' + str(count) + '\n')
print('total errors:', count)
readme.close()
file_log.close()



            

