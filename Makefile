install:
	uv sync

update:
	uv tool install --force dist/hexlet_code-0.1.0.tar.gz

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games