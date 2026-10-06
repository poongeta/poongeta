from pathlib import Path
from wordcloud import WordCloud

words = [line.strip() for line in Path("words.txt").read_text().splitlines() if line.strip()]
sizes = {word: len(words) + 5 - i for i, word in enumerate(words)}

themes = {
    "light": ["#0969da", "#8250df", "#bf3989", "#1a7f37", "#bc4c00"],
    "dark": ["#58a6ff", "#bc8cff", "#ff7b72", "#3fb950", "#d29922"],
}

for name, colors in themes.items():
    def pick_color(word, **rest):
        return colors[words.index(word) % len(colors)]

    cloud = WordCloud(
        width=900,
        height=400,
        mode="RGBA",
        background_color=None,
        color_func=pick_color,
        relative_scaling=1,
        max_font_size=100,
        prefer_horizontal=1,
        random_state=1,
    )
    cloud.generate_from_frequencies(sizes).to_file(f"cloud-{name}.png")
