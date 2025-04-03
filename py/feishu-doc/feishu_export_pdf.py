import requests
import time
import os

# -----------------------
# 配置区域，请替换为实际参数
# -----------------------
TENANT_ACCESS_TOKEN = "your_tenant_access_token"
TENANT_ACCESS_TOKEN = "u-eO2y9hCbd7KWISmrX1oysA40ns7x1hRzNq20ggQ02a9w"
TENANT_ACCESS_TOKEN = "u-eJBlCPMLZb5VIA2BwCysPBgl6d_11hn3oG00g0c00EMc"
TENANT_ACCESS_TOKEN = "u-f0v1EC.ft1PrWf7lK5CrqAh0gQEh1hn1M2000lcw0yhN"

# 通过下面这个来刷新user access token.
# https://open.feishu.cn/api-explorer/cli_a73b9e948038500b?apiName=search&from=op_doc_tab&project=bitable&resource=app.table.record&version=v1

HEADERS = {
    "Authorization": f"Bearer {TENANT_ACCESS_TOKEN}",
    "Content-Type": "application/json",
}
# 搜索接口地址、导出任务接口地址及下载接口地址（请参考飞书官方文档，如有更新请调整）
SEARCH_URL = "https://open.feishu.cn/open-apis/suite/docs-api/search/object"
EXPORT_TASK_URL = "https://open.feishu.cn/open-apis/drive/v1/export_tasks"
DOWNLOAD_URL_TEMPLATE = "https://open.feishu.cn/open-apis/drive/v1/{api_path}"


# -----------------------
# 1. 搜索包含关键字的文档
# -----------------------
def search_documents(keyword, limit=10):
    params = {
        "search_key": keyword,
        "count": limit,
        "offset": 0,
        "docs_types": ["doc", "file"],
    }
    print(params)
    # response = requests.post(SEARCH_URL, headers=HEADERS, params=params)
    response = requests.post(SEARCH_URL, headers=HEADERS, json=params)
    if response.status_code != 200:
        print("搜索接口调用失败：", response.text)
        return []
    data = response.json()
    print(data)
    files = data.get("data", {}).get("docs_entities", [])
    return files


# -----------------------
# 2. 创建导出任务，转换为 PDF 格式
# -----------------------
def create_export_task(file_token, export_format="pdf"):
    payload = {"token": file_token, "type": "docx", "file_extension": export_format}
    response = requests.post(EXPORT_TASK_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        print("创建导出任务失败：", response.text)
        return None
    data = response.json()
    print(data)
    ticket = data.get("data", {}).get("ticket")
    return ticket


# -----------------------
# 3. 查询导出任务状态，直到任务完成
# -----------------------
def poll_export_task(file_token, ticket, poll_interval=5, timeout=240):
    print("running poll_export_task")
    poll_url = f"{EXPORT_TASK_URL}/{ticket}?token={file_token}"
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = requests.get(poll_url, headers=HEADERS)
        if response.status_code != 200:
            print("查询任务状态失败：", response.text)
            return None
        data = response.json()
        print(data)
        code = data.get("code")
        if code == 0:
            status = data.get("data", {}).get("result").get("job_status")
            if status == 0:
                # 返回导出的文件 token
                return data.get("data", {}).get("result").get("file_token")
            elif status >= 3:
                print("导出任务失败。")
                return None
        else:
            print("导出任务失败。")
            return None
        # 继续等待
        time.sleep(poll_interval)
    print("导出任务超时。")
    return None


# -----------------------
# 4. 下载导出后的文件
# -----------------------
def download_file(file_token, save_path):
    # 生成下载链接，此处假设下载接口路径为 export_tasks/file/{file_token}/download
    download_api_path = f"export_tasks/file/{file_token}/download"
    download_url = DOWNLOAD_URL_TEMPLATE.format(api_path=download_api_path)
    response = requests.get(download_url, headers=HEADERS, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"文件已下载至 {save_path}")
    else:
        print("下载文件失败：", response.text)


# -----------------------
# 主流程
# -----------------------
def main(keyword, limit=50):
    print(f"正在搜索包含关键字 '{keyword}' 的文档...")
    files = search_documents(keyword, limit=50)
    if not files:
        print("未找到匹配的文档。")
        return

    # 这里我们按文件列表逐一处理
    for file_info in files:
        file_token = file_info.get("docs_token")
        file_title = file_info.get("title")
        file_name = "token_pdf/token_" + file_token + ".pdf"
        if not file_token:
            continue
        if os.path.exists(file_name):
            print("已经下载过了!!! " + file_name)
            continue

        print(f"处理文件：{file_title} ({file_token})")
        # 创建导出任务
        ticket = create_export_task(file_token, export_format="pdf")
        if not ticket:
            print("跳过文件。")
            continue
        print(f"创建导出任务成功，ticket: {ticket}")
        # 等待任务完成并获取导出后的文件 token
        exported_file_token = poll_export_task(file_token, ticket)
        if not exported_file_token:
            print("导出任务未成功完成，跳过文件。")
            continue
        # 设置保存路径
        save_path = file_name
        # 下载文件
        download_file(exported_file_token, save_path)
        print("----------------------------------------------------")


def main2():
    customers = "yuno,atlassian,bamboo-hr,broscorp,celonis,cipherowl,conductor,demandbase,expedia,fanatics,gocode,hellasdirect,intuit,jedlix,metica,paysafe,peer39,puppygraph,splitmetrics,swiggy,verisoul,weave,abjayon,aeg-vision,apple,aurora,cvs,edgetotrade,harness,microsoft,targit,grab,shopee".split(
        ","
    )
    customers = []
    keywords = [
        "RCA",
        "oom issue",
        "crash issue",
        "stuck issue",
        "hang issue",
        "事故分析",
        "Crash分析",
        "OOM分析",
        "卡顿分析",
        "死锁分析",
        "Root Cause Analysis",
        "性能分析",
        "性能优化",
        "性能调优",
        "性能瓶颈",
        "性能问题",
        "设计文档",
        "架构文档",
        "设计规范",
    ]
    for keyword in customers + keywords:
        main(keyword, limit=50)


if __name__ == "__main__":
    main2()
