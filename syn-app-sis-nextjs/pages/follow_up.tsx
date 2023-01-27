'use client';
import { Inter } from '@next/font/google'
import { useRouter } from 'next/navigation';


const inter = Inter({ subsets: ['latin'] })

export default function followUp() {
  const router = useRouter();
  return (
    <main  className="max-w-flex min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 ">
      <div>

        <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">FOLLOW UP FORM </h2>
        <p className="mt-2 text-center text-sm text-gray-600">
        
          <button
            onClick={() => router.push("/")}
            type="button"
            className="group relative flex-center justify-center
            py-2 px-4 border border-transparent text-sm font-medium
            rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
          >
           Zakończ ankietę
          </button>


        </p>
      </div>
    </main>
  )
}
