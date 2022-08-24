import datetime
import api
import markdown
import os

from typing import Any, Dict
from bs4 import BeautifulSoup


def run() -> None:
    title = _get_target_title()
    if title is None:
        raise ValueError("There must be only one upload article.")

    html = _convert_md_to_html(title)
    tag = _extract_tag(html)

    result = api.post_write(title=title, content=str(html), tag=tag, visibility=0)
    if result.get("tistory") is None:
        raise ValueError("Upload failed.")

    send_message(result)


def _get_target_title() -> str:
    # TODO: 추후 복수의 파일도 업로드할 수 있도록 변경예정
    file_arr = os.listdir("upload/.")
    if len(file_arr) > 1:
        return
    title = file_arr.pop().rstrip(".md")
    return title


def _convert_md_to_html(title: str) -> Dict[str, Any]:
    with open(f"upload/{title}.md", "r") as f:
        text = f.read()
        html = markdown.markdown(text, extensions=["fenced_code"])
        return BeautifulSoup(html, "html.parser")


def _extract_tag(html: str) -> str:
    head_tag = [h1.text for h1 in html.find_all("h1")]
    tail_tag = [html.tag.extract().text] if html.tag else []
    tag = ",".join(head_tag + tail_tag)
    return tag


def send_message(result: Dict[str, Any]) -> None:
    now = datetime.datetime.now()
    message = {
        "content": f"시간 : {now.strftime('%Y-%m-%d %H:%M:%S')} \n결과 : {result['tistory'].get('url')}"
    }
    api.send_message_to_discord(message)


if __name__ == "__main__":
    run()
