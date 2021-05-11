import re

from pygments.lexer import RegexLexer
from pygments.token import Text, Keyword, Name, String, Operator, Punctuation, Comment
from pygments.lexers.haskell import HaskellLexer


class UnnamedLexer(RegexLexer):
    name = "Unnamed"
    aliases = ["unnamed"]
    filenames = ["*.unnamed"]
    mimetypes = ["text/x-unnamed"]

    identChar = '[^\s(){};\\."]'

    tokens = {
        "root": [
            (r"\s+", Text),
            (r"--.*$", Comment.Single),
            (r"\{-", Comment.Multiline, "comment"),
            (r"[(){};]", Punctuation),
            (r"\\", Keyword.Reserved),
            (r"\.-?", Operator),
            (r'"', String, "string"),
            (fr"(=|:|→|->|\||:=)(?!{identChar})", Operator.Word),
            (fr"(_|let|∀|forall|λ|#|rec)(?!{identChar})", Keyword.Reserved),
            (fr"(U|Row|Rec)(?!{identChar})", Keyword.Type),
            (fr"{identChar}+", Name),
        ],
        "comment": HaskellLexer.tokens["comment"],
        "string": HaskellLexer.tokens["string"],
        "escape": HaskellLexer.tokens["escape"],
    }
