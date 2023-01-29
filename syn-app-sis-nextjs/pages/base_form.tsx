import { useRouter } from 'next/navigation';
import Modal from '@/components/modal';

import React, { Fragment, useState } from "react";

export const getStaticProps = async () =>{
  const res = await fetch("http://127.0.0.1:8000/api/baseQuestionList/");
  const data = await res.json();

  return {
    props: {questions: data}
  }
}


const base_form = ({questions}) => {
  //console.log(questions);

  const [showModal, setShowModal] = useState(false);

  const router = useRouter();

  const map_question_answer = (answers) =>
  {
    
    let mapped_questions = {}
    let question_id = 0
    let score = 0
    let answer
    for(let idx = 0; idx < answers.length-1 ; idx++)
    {
      
      console.log("ID", idx)
      if(answers[idx].id.includes("yes")){
        console.log("yes")
      }
      if (answers[idx].checked == true) {
        if(answers[idx].id.includes("yes")) {
          answer = true
        }
        else{
          answer = false
        } 
        // we need to change scoring to opposite for some questions
        if (questions["questions"][question_id]["pass_choise"] == true ){
          answer = !answer
        }
        
        if (answer == true){
          score++
        }
        mapped_questions[questions["questions"][question_id]["id"]] = answer
        question_id++
      }    
    }
    mapped_questions["score"] = score
    return mapped_questions
  }


  const handleSubmit = (e) => {
    e.preventDefault()
    let data_to_db = map_question_answer(e.target)


    data_to_db["postal_code"] = document.querySelector('#code').value
    data_to_db["birth_date"] = document.querySelector('#date').value


    console.log(data_to_db)
    //fetch POST
    if(data_to_db["score"] <=2){
      setShowModal(true)
    }
    else{
     router.push('/follow_up')
    }

  }

  return (
    <main className=" w-screen flex item-center justify-center m-10">

      <div>
      
        <h1 className="mt-6 text-center text-3xl font-extrabold text-gray-900 py-12 px-4 sm:px-6 lg:px-8 ">
          Wypełnij wszystkie pola
        </h1>
        <form onSubmit={handleSubmit} >
        <Fragment>
        <div className=" flex items-center mb-4 space-x-3" >
        <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Kod pocztowy</label>
        <input type="text" id="code" name="code" className="inline-flex items-center border-2"required />
        <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Data urodzenia</label>
        <input type="date" id="date" name="date"  className="inline-flex items-center border-2 "required />
        </div>
          {questions["questions"].map(question => (
            <div className='border-2 py-2 px-4 sm:px-6 lg:px-8' key={question.id} >
              <a>
                <h3>{question.question_no}. {question.question_text_pl}</h3>
              </a>
          
          <div className=" flex items-center mb-4 space-x-3 rounded-md" >
            <input type="radio" name={question.id} id={"yes"+question.id} className="inline-flex items-center"required/> 
              <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Tak</label>
            <input type="radio"name={question.id} id={"no"+question.id} className="inline-flex items-center " required/> 
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
          <Modal isVisible={showModal}></Modal>
          </Fragment>
        </form>
      </div>

    </main>
  );
};
  
export default base_form;