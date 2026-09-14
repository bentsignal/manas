import Reader from './reader';
import manifest from '../public/text/manifest.json';
import initialLines from '../public/text/initial.json';
export default function Home(){ return <Reader manifest={manifest} initialLines={initialLines}/>; }
