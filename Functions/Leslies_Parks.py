def to_be_built(votes_in_favor, votes_against):
    if votes_in_favor >= 2 * votes_against:
        return "YES"
    else:
        return "NO"

print(to_be_built(100,40))