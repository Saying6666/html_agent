# Generation Notes

1. Open your target generator, such as Pencil.dev or Cursor.
2. Paste `prompt.md` round by round.
3. Ask the tool to return only the final `index.html`.
4. Save the generated HTML into `src/index.html`.
5. Run `python skills/web-design-dataset-pipeline/scripts/validate_task.py fdu_003 --stage final` before packaging.
