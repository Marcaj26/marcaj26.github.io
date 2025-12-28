from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import re


def extract_and_normalize_soundcloud(embed_html: str) -> str:
    # 1. Extract iframe src
    match = re.search(r'src="([^"]+)"', embed_html)
    if not match:
        raise ValueError("No iframe src found")

    url = match.group(1)

    # 2. Parse URL
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    # 3. Force desired parameters
    params["color"] = ["#6828a4"]
    params["auto_play"] = ["false"]
    params["hide_related"] = ["true"]
    params["show_comments"] = ["false"]
    params["show_user"] = ["true"]
    params["show_reposts"] = ["false"]
    params["show_teaser"] = ["false"]
    params["visual"] = ["true"]

    # 4. Rebuild clean URL
    new_query = urlencode(params, doseq=True)
    clean_url = urlunparse(parsed._replace(query=new_query))

    return clean_url


# Example usage
before_embed = """<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/soundcloud%253Atracks%253A2237700518&color=%23a16e3c&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/marc-johansen-840272710" title="Marc Johansen" target="_blank" style="color: #cccccc; text-decoration: none;">Marc Johansen</a> · <a href="https://soundcloud.com/marc-johansen-840272710/trapbeat_138bpm_d-min" title="TrapBeat_138bpm_D#Min" target="_blank" style="color: #cccccc; text-decoration: none;">TrapBeat_138bpm_D#Min</a></div>"""

print(extract_and_normalize_soundcloud(before_embed))
