import React from "react";


const Modal = ({isVisible, score}) => {
  if( !isVisible) return null;
  return(
    <div className="fixed inset-0 bg-black bg-opacity-25 backdrop-blur-sm flex justify-center items-center">
      <div className="w-[600px]">
        <div className="bg-white p-2 rounded">Dziękujemy za wypełnienie formularza. Wynik to {score}</div>

      </div>
    </div>
  )

}

export default Modal