import '../public/globals.css'
import { Lato } from '@next/font/google'
const lato = Lato({ weight:['400', '700'], subsets: ['latin'] })
export default function App({ Component, pageProps }) 
{  
    return <main className={ lato.className }> <Component { ...pageProps } />  </main>
}