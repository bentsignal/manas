import {rm} from 'node:fs/promises';

// vinext can retain old copied assets between builds. Deploy only current assets.
await rm(new URL('../dist/',import.meta.url),{recursive:true,force:true});
