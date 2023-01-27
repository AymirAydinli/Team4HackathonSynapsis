import React from "react";
import { useRouter } from 'next/navigation';

export const getStaticProps = async () =>{
  const res = await fetch("http://127.0.0.1:8000/api/get_base_questions/");
  const data = await res.json();

  return {
    props: {questions: data}
  }
}
   
const base_form = ({questions}) => {
  //console.log(questions);
  const router = useRouter();
  const sum = (input) =>{
    let points = 0 


    return points
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(e)

    //document.getElementById('0').target.checked
    // console.log(e.target["0"].checked)
    // console.log(e.target["1"].checked)
    // console.log(e.target["2"].checked)
    // console.log(e.target["3"].checked)
    // console.log( e.target.length)
    
    for(let idx = 0; idx < e.target.length-1 ; idx++)
    {
      console.log(e.target[idx].checked)
    }

    const sumPoints = sum(e)

    //fetch POST
    if(sumPoints >=3){

    }
    else{router.push('/follow_up')}

  }

  return (
    <main className=" w-screen flex item-center justify-center m-10">
      <div>
      
        <h1 className="mt-6 text-center text-3xl font-extrabold text-gray-900 py-12 px-4 sm:px-6 lg:px-8 ">
          Wypełnij wszystkie pola
        </h1>
        <form onSubmit={handleSubmit} >
          {questions["questions"].map(question => (
            <div key={question.id}>
              <a>
                <h3>{question.id}. {question.pl}</h3>
              </a>
          <div className=" flex items-center mb-4 space-x-3" >
            <input type="radio" name={question.id} id={question.id} className="inline-flex items-center "/> 
              <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Tak</label>
            <input type="radio"name={question.id} className="inline-flex items-center "/> 
              <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Nie</label>
          </div>
            </div>
          ))

          }
          <input type='submit'
            className="group relative flex-center justify-center
            py-2 px-4 border border-transparent text-sm font-medium
            rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
            value='Zakończ ankietę' 
          />

        </form>
      </div>

    </main>
  );
};
  
export default base_form;