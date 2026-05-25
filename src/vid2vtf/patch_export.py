

from srctools.tokenizer import BARE_DISALLOWED, Tokenizer as Tokenizer
from srctools.types import FileWText
def patch_export(self, f: FileWText, quote=False) -> None:
        """Write the material back to a file."""
        f.write(self.shader + '\n\t{\n')
        for param in self._params.values():
            name = param.name
            value = param.value
            if any(c in BARE_DISALLOWED for c in name) or quote:
                name = f'"{name}"'
            if not value or any(c in BARE_DISALLOWED for c in value) or quote:
                value = f'"{value}"'
            f.write(f'\t{name} {value}\n')
        for block in self.blocks:
            block.serialise(f, start_indent='\t')
        if self.proxies:
            f.write('\n\tProxies\n\t\t{\n')
            for block in self.proxies:
                block.serialise(f, start_indent='\t\t')
            f.write('\t\t}\n')
        f.write('\t}\n')