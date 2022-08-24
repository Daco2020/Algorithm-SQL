import requests
import orjson

from typing import Any, Dict, Optional
from config import ACCESS_TOKEN, BLOG_NAME, API_URL, DISCORD_WEBHOOK_URL


common_params = {"access_token": ACCESS_TOKEN, "output": "json", "blogName": BLOG_NAME}


def get_post_list(page: Optional[int] = 1) -> Dict[str, Any]:
    res = requests.get(
        f"{API_URL}/post/list?",
        params={"page": page, **common_params},
    )
    return orjson.loads(res.text)


def get_post_read(post_id: str):
    res = requests.get(
        f"{API_URL}/post/read?",
        params={"postId": post_id, **common_params},
    )
    return orjson.loads(res.text)


def post_write(
    title: str,
    content: str,
    tag: Optional[str] = None,
    slogan: Optional[str] = None,
    password: Optional[str] = None,
    published: Optional[int] = None,
    visibility: Optional[int] = 3,
    category_id: Optional[int] = 0,
    accept_comment: Optional[int] = 1,
) -> Dict[str, Any]:
    option_params = _check_options(
        tag,
        slogan,
        password,
        published,
        visibility,
        category_id,
        accept_comment,
    )
    res = requests.post(
        f"{API_URL}/post/write?",
        params={
            "title": title,
            "content": content,
            **option_params,
            **common_params,
        },
    )
    return orjson.loads(res.text)


def post_modify(
    post_id: str,
    title: str,
    content: str,
    tag: Optional[str] = None,
    slogan: Optional[str] = None,
    password: Optional[str] = None,
    published: Optional[int] = None,
    visibility: Optional[int] = 3,
    category_id: Optional[int] = 0,
    accept_comment: Optional[int] = 1,
) -> Dict[str, Any]:
    option_params = _check_options(
        tag,
        slogan,
        password,
        published,
        visibility,
        category_id,
        accept_comment,
    )
    res = requests.post(
        f"{API_URL}/post/modify?",
        params={
            "postId": post_id,
            "title": title,
            "content": content,
            **option_params,
            **common_params,
        },
    )
    return orjson.loads(res.text)


def _check_options(
    tag: Optional[str],
    slogan: Optional[str],
    password: Optional[str],
    published: Optional[int],
    visibility: Optional[int],
    category_id: Optional[int],
    accept_comment: Optional[int],
):
    option_params = {}
    if tag:  # 태그(',' 로 구분)
        option_params.update({"tag": tag})
    if slogan:  # 문자 주소
        option_params.update({"slogan": slogan})
    if password:  # 보호글 비밀번호
        option_params.update({"password": password})
    if published:  # 발행시간(TIMESTAMP 이며 미래의 시간을 넣을 경우 예약. 기본값: 현재시간)
        option_params.update({"published": published})
    if visibility:  # 공개여부(0: 비공개 - 기본값, 1: 보호, 3: 발행)
        option_params.update({"visibility": visibility})
    if category_id:  # 카테고리 아이디(기본값: 0)
        option_params.update({"category": category_id})
    if accept_comment:  # 댓글 허용(0, 1 - 기본값)
        option_params.update({"acceptComment": accept_comment})
    return option_params


def send_message_to_discord(message: Dict[str, Any]) -> None:
    res = requests.post(DISCORD_WEBHOOK_URL, data=message)
