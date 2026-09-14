import type { Metadata } from 'next';
import {headers} from 'next/headers';
import './globals.css';
export async function generateMetadata():Promise<Metadata>{
 const h=await headers();
 const host=h.get('host')||'manas-every-line.sassy-river-6779.chatgpt.site';
 const protocol=host.startsWith('localhost')?'http':'https';
 const origin=new URL(`${protocol}://${host}`);
 const title='Manas — Every line';
 const description='A project to translate the complete Sayakbay Karalaev corpus into English. Source verification is in progress; no complete translation is claimed.';
 return {metadataBase:origin,title,description,openGraph:{title,description,type:'website',images:[{url:new URL('/og.png',origin).href,width:1536,height:1024,alt:'Manas — Every line. The Karalaev translation project. Edition in preparation.'}]},twitter:{card:'summary_large_image',title,description,images:[new URL('/og.png',origin).href]}};
}
export default function RootLayout({children}:{children:React.ReactNode}) {
 return <html lang="en"><body>{children}</body></html>;
}
