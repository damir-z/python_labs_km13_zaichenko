import json

with open("image_info_test-dev2017.json", "r") as file:
    data = json.load(file)
    print(f"Total amount of images in file is {len(data['images'])}.")
    print(f"Total amount of categories in file is {len(data['categories'])}.")
    for image in data["images"]:
        if image["file_name"] == "000000000001.jpg":
            print(f'\nfile_name = "000000000001.jpg"\n'
                  f"    url: {image['coco_url']}\n    width: {image['width']}\n"
                  f"    height: {image['height']}\n    id: {image['id']}\n")

    nums = [data["images"][i]["file_name"] for i in range(len(data["images"]))]
    print(f'A photo with max number is "{max(nums)}".')