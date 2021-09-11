## Python Tips

### `Counter` vs `defaultdict`

> https://stackoverflow.com/a/19883180

Key difference: 

- `Counter` won't add new keys to the dict when you query for missing keys. So, if your queries include keys that may not be present in the dict then better use `Counter`.

However, `Counter` is slower than `defaultdict` :

> https://stackoverflow.com/a/27802189

