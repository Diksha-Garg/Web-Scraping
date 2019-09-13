from bs4 import BeautifulSoup
import urllib.request
import requests
import threading
import time
img_count = 0
def img_save(img_url):
    # print(img_url)
    global img_count
    img_count +=1
    file_name = "image" + str(img_count)
    # print(file_name)
    url = img_url
    full_path = "C:/Users/diksha.garg/Pictures/Saved Pictures/" + file_name + ".jpg"
    print(full_path)
    try:
        urllib.request.urlretrieve(url, full_path)
        # print(full_path)
    except Exception as e:
        pass
if __name__ == '__main__':
    t = time.time()
    req = requests.get('http://www.thrillophilia.com/blog/60-places-you-need-to-visit-in-india-with-your-best-friend/')
    output = req.text
    # print(output)
    soup = BeautifulSoup(output, 'html.parser')
    list_images = []
    rows = soup.findAll('img')
    # print(rows)
    # print(rows['src'])
    j = 0

    for row in rows :
        list_images.append(str(row['src']))
    # for index in list_images:
    #     print(index)
    # print(row['src'])
    # q.put(str(row['src']))
    # for index in list_images:
    #     print(index)
    # print(type(list_images))
    threads_list = []
    for img_url in range(len(list_images) -1 ):
        # print(list_images[img_url])
        # img_save(list_images[img_url])
        t1 = threading.Thread(target=img_save, args=(list_images[img_url],))
        threads_list.append(t1)
        t1.start()
        # t1.join()
    for ts in threads_list:
        ts.join()
        print("Thread has joined",ts.name)
    print("Time taken ", time.time() - t)



# import  concurrent.futures
#
# with concurrent.futures.ThreadPoolExecutor as executor:
#     executor.map(img_save, list_images)
