import React from "react";

export const getStaticProps = async () =>{
  const res = await fetch("http://127.0.0.1:8000/api/get_base_questions/");
  const data = await res.json();

  return {
    props: {questions: data}
  }
}
   
const base_form = ({questions}) => {
  //console.log(questions);

  return (
    <main className=" w-screen flex item-center justify-center m-10">
      <div>
      
        <h1 className="mt-6 text-center text-3xl font-extrabold text-gray-900 py-12 px-4 sm:px-6 lg:px-8 ">
          Wypełnij wszystkie pola
        </h1>
        <div >
          {questions["questions"].map(question => (
            <div key={question.id}>
              <a>
                <h3>{question.id}. {question.pl}</h3>
              </a>
          <div className=" flex items-center mb-4 space-x-3" >
            <input type="radio" value="Male" name={question.id} className="inline-flex items-center "/> 
              <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Tak</label>
            <input type="radio" value="Female" name={question.id} className="inline-flex items-center "/> 
              <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Nie</label>
          </div>
            </div>
          ))

          }
        </div>
      </div>
    </main>
  );
};
  
export default base_form;