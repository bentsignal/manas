import Reader from './reader';
import target from '../corpus/target.json';
import manifest from '../public/text/manifest.json';
export default function Home(){ return <Reader manifest={manifest} parts={target.parts}/>; }
