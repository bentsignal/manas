import Reader from './reader';
import manifest from '../public/text/manifest.json';
export default function Home(){ return <Reader manifest={manifest}/>; }
