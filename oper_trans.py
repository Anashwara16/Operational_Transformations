import json


def is_valid(stale, latest, ot_json):
    try:
        operations = json.loads(ot_json)
    except ValueError:
        return False
    processed_stale = stale
    current_cursor_pos = 0

    for operation in operations:
        if operation["op"] == "skip":
            skip_cursor_pos = operation.get("count")
            if skip_cursor_pos is None:
                return False
            stale_length = len(processed_stale)
            current_cursor_pos = skip_string(
                stale_length, current_cursor_pos, skip_cursor_pos
            )
            if current_cursor_pos is None:
                return False

        elif operation["op"] == "insert":
            insert_str = operation.get("chars")
            if insert_str is None:
                return False
            processed_stale, updated_cursor_pos = insert_string(
                processed_stale, current_cursor_pos, insert_str
            )
            if processed_stale is None:
                return False
            current_cursor_pos = updated_cursor_pos

        elif operation["op"] == "delete":
            delete_count = operation.get("count")
            if delete_count is None:
                return False
            processed_stale, updated_cursor_pos = delete_string(
                processed_stale, current_cursor_pos, delete_count
            )
            if processed_stale is None:
                return False
            current_cursor_pos = updated_cursor_pos

    return processed_stale == latest


def skip_string(stale_length, current_cursor_pos, skip_cursor_pos):
    updated_cursor_pos = current_cursor_pos + skip_cursor_pos
    return updated_cursor_pos if updated_cursor_pos <= stale_length else None


def insert_string(processed_stale, current_cursor_pos, insert_str):
    if current_cursor_pos > len(processed_stale):
        return None, None

    if current_cursor_pos == len(processed_stale):
        updated_stale = processed_stale + insert_str
        updated_cursor_pos = current_cursor_pos + len(insert_str)
        return updated_stale, updated_cursor_pos

    before_insert_string = processed_stale[:current_cursor_pos]
    end = len(processed_stale)
    after_insert_string = processed_stale[current_cursor_pos:end]
    updated_stale = before_insert_string + insert_str + after_insert_string
    updated_cursor_pos = current_cursor_pos + len(insert_str)
    return updated_stale, updated_cursor_pos


def delete_string(processed_stale, current_cursor_pos, delete_count):
    continue_cursor_pos = current_cursor_pos + delete_count

    if continue_cursor_pos > len(processed_stale):
        return None, None

    before_deleted = processed_stale[:current_cursor_pos]
    after_deleted = processed_stale[current_cursor_pos:]

    updated_stale = before_deleted + after_deleted
    updated_cursor_pos = 0 if not before_deleted else current_cursor_pos

    return updated_stale, updated_cursor_pos


if __name__ == "__main__":
    result = is_valid(
        "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
        "Repl.it uses operational transformations.",
        '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]',
    )
    print(result)
