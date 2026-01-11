#!/usr/bin/env python3
import json
import os
import sys
import urllib.request
import urllib.error


def send_dingtalk_notification(
    webhook_url: str,
    status: str,
    job_name: str,
    build_number: str,
    build_url: str
) -> bool:
    """
    发送钉钉通知

    Args:
        webhook_url: 钉钉机器人 Webhook 地址
        status: 构建状态 (success/failure)
        job_name: Jenkins 任务名
        build_number: 构建号
        build_url: 构建页面 URL

    Returns:
        bool: 发送成功返回 True，失败返回 False
    """
    status_text = "成功" if status == "success" else "失败"
    status_emoji = "✅" if status == "success" else "❌"

    message = {
        "msgtype": "markdown",
        "markdown": {
            "title": f"UI 自动化测试{status_text}",
            "text": f"""## {status_emoji} UI 自动化测试{status_text}

- **项目**: {job_name}
- **构建号**: #{build_number}
- **状态**: {status_text}

[📊 查看 Allure 报告]({build_url}allure)

[🔗 查看构建详情]({build_url})
"""
        }
    }

    try:
        data = json.dumps(message).encode("utf-8")
        req = urllib.request.Request(
            webhook_url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))
            if result.get("errcode") == 0:
                print(f"钉钉通知发送成功: {status_text}")
                return True
            else:
                print(f"钉钉通知发送失败: {result.get('errmsg')}")
                return False
    except urllib.error.URLError as e:
        print(f"钉钉通知发送失败: {e}")
        return False
    except Exception as e:
        print(f"钉钉通知发送失败: {e}")
        return False


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: python dingtalk.py <success|failure>")
        sys.exit(1)

    status = sys.argv[1]
    if status not in ("success", "failure"):
        print("Status must be 'success' or 'failure'")
        sys.exit(1)

    webhook_url = os.getenv("DINGTALK_WEBHOOK")
    if not webhook_url:
        print("Error: DINGTALK_WEBHOOK environment variable not set")
        sys.exit(1)

    job_name = os.getenv("JOB_NAME", "UI-Automation-Test")
    build_number = os.getenv("BUILD_NUMBER", "0")
    build_url = os.getenv("BUILD_URL", "http://localhost:8080/")

    success = send_dingtalk_notification(
        webhook_url=webhook_url,
        status=status,
        job_name=job_name,
        build_number=build_number,
        build_url=build_url
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
