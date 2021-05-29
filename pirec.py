from pygments.lexer import RegexLexer
from pygments.token import Text, Keyword, Name, String, Operator, Punctuation, Comment
from pygments.lexers.haskell import HaskellLexer


class PirecLexer(RegexLexer):
    name = "Pirec"
    aliases = ["pirec"]
    filenames = ["*.pirec"]
    mimetypes = ["text/x-pirec"]

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
            (fr"(=|:|→|->|×|&|,|\||:=)(?!{identChar})", Operator.Word),
            (
                fr"(_|let|∀|forall|λ|∃|exists|proj1|proj2|#|rec)(?!{identChar})",
                Keyword.Reserved,
            ),
            (fr"(Type|Row|Rec)(?!{identChar})", Keyword.Type),
            (fr"{identChar}+", Name),
        ],
        "comment": HaskellLexer.tokens["comment"],
        "string": HaskellLexer.tokens["string"],
        "escape": HaskellLexer.tokens["escape"],
    }
