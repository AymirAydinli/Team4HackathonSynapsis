import React from "react";
import { useRouter } from 'next/navigation';

const Modal = ({isVisible}) => {
  const router = useRouter();
  if( !isVisible) return null;
  return(
    <main>

    <div className="fixed inset-0 bg-black bg-opacity-25 backdrop-blur-sm flex justify-center items-center">
      <div className="w-[600px]">
        <div className="bg-white p-2 rounded">Dziękujemy za wypełnienie formularza. Nie jest wymagane dalsze działanie monitorujące pod kątem ASD. Zaleca się ponowną obserwację po skończeniu przez dziecko 2. roku życia.
        <div className=" flex justify-center items-center p-2">
        <button
            onClick={() => router.push("/")}
            type="button"
            className="group relative flex-center justify-center
            py-2 px-4 border border-transparent text-sm font-medium
            rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
          >
           Zakończ ankietę
          </button>
        </div>
        </div>

      </div>
      
    </div>

    </main>
    
  )

}

export default Modal