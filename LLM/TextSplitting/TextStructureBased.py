from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space is a vast, mysterious expanse that has fascinated humanity since the beginning of time. It stretches beyond the limits of our imagination, holding countless galaxies, stars, and planets that inspire curiosity and exploration. The night sky that we see is only a tiny fraction of what exists, with billions of stars twinkling like distant beacons. Scientists believe that the universe is constantly expanding, making it an ever-changing canvas of wonders. Space is not just empty darkness; it is filled with energy, radiation, and celestial bodies moving with the laws of physics. The vacuum of space challenges human survival, yet it pushes us to test the limits of science. From ancient stargazers to modern astronomers, the quest to understand space has shaped culture and knowledge. Every discovery, whether a black hole or a new planet, adds to our story of the cosmos. Space remains a symbol of the unknown, reminding us of how small yet significant we are. Its mysteries are endless, and our journey to uncover them has only just begun.

When we talk about space exploration, it represents humanity’s drive to reach beyond the known. Rockets breaking through Earth’s atmosphere marked the first steps, leading to the moon landing and orbiting stations. These milestones reflect not only technology but also human perseverance and ambition. Exploration has taught us about Earth’s origins, the possibilities of life elsewhere, and the mechanics of the universe. Satellites orbiting Earth provide weather forecasts, navigation, and global communication that shape our daily lives. Dreams of colonizing Mars or building bases on the Moon reflect our desire to expand beyond our planet. Despite radiation, microgravity, and scarce resources, innovation keeps pushing solutions forward. The International Space Station stands as a symbol of global unity and shared knowledge. Each mission teaches lessons about resilience, science, and cooperation that go beyond borders. Exploring space is not just about reaching worlds but about understanding our own better.

Philosophically, space makes us reflect on life, time, and existence itself. Looking at the night sky often fills us with awe, wonder, and humility at the same time. The vastness of the cosmos makes daily struggles feel small, yet highlights the beauty of our fragile Earth. Space forces us to ask questions of creation, whether answered through science or spirituality. The idea of extraterrestrial life excites imagination and sparks debates about whether we are alone. For centuries, artists and poets have used space as a metaphor for dreams and infinite possibilities. Many revolutions in technology began with the dream of reaching beyond Earth. The cosmos reminds us that our planet is a rare and delicate home among the stars. In exploring it, we also explore the essence of humanity and our place in the universe. Space is not only a frontier of science but also a timeless source of inspiration and discovery.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)

splits = splitter.split_text(text)

print(splits)
