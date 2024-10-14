import os
from app.dbs.nosqldb import tuxi2_font_md5
from app import file_storge

# 查询所有记录
try:
    records = tuxi2_font_md5.find()
    ids_to_delete = []  # 用于存储需要删除的记录的 ID

    for record in records:
        font_url = record.get('font_url')

        # 检查 font_url 是否为字符串
        if isinstance(font_url, str):
            # 提取文件名
            file_name = os.path.basename(font_url)

            try:
                # 获取文件的 Content-Length
                response = file_storge.client.head_object(Bucket='tuxi-1301633205', Key=file_name)
                content_length = response['Content-Length']

                # 检查 Content-Length 是否为 0
                if content_length == 0:
                    ids_to_delete.append(record['_id'])  # 收集需要删除的 ID
                    print("Found zero length file: {}".format(file_name))

            except Exception as e:
                print("Error checking {}: {}".format(file_name, e))
        else:
            print("Invalid font_url for record {}: {}".format(record['_id'], font_url))

    # # 批量删除记录
    # if ids_to_delete:
    #     tuxi2_font_md5.remove({'_id': {'$in': ids_to_delete}})
    #     print("Deleted records with zero length files: {}".format(ids_to_delete))
    # else:
    #     print("No records with zero length files found.")

except Exception as e:
    print("Error occurred while fetching records: {}".format(e))