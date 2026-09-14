import {createHash} from 'node:crypto';

export function encodeTextChunks(rows,chunkSize=256){
 if(!Number.isInteger(chunkSize)||chunkSize<1)throw new Error('Invalid chunk size');
 const chunks=[];
 for(let i=0;i<rows.length;i+=chunkSize){
  const text=JSON.stringify(rows.slice(i,i+chunkSize))+'\n';
  chunks.push({hash:createHash('sha256').update(text).digest('hex'),text});
 }
 return chunks;
}
