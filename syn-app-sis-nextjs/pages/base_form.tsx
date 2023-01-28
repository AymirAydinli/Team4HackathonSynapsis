//import React from "react";
import { useRouter } from 'next/navigation';
import Modal from '@/components/modal';

import React, { Fragment, useEffect, useRef, useState } from "react";

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
  const sum = (input) =>{
    let points = 0 
    console.log( input)

    return points
  }

  const map_question_answer = (answers) =>
  {
    let mapped_questions = {}
    let question_id = 0
    let score = 0
    let answer
    for(let idx = 0; idx < answers.length-1 ; idx++)
    {
      console.log("ID", idx)
      if (answers[idx].checked == true) {
        if( idx % 2 == 0) {
          answer = false
        }
        else{
          answer = true
        } 
        console.log("PASSSS", questions["questions"][question_id]["pass_choise"])
        // we need to change scoring to opposite for some questions
        console.log(questions["questions"][question_id]["pass_choise"])
        if (questions["questions"][question_id]["pass_choise"] == true ){
          if (answer == false){
            answer = true
          }
          else{
            answer = false
          }
        }
        
        if (answer == true){
          score++
        }
        mapped_questions[questions["questions"][question_id]["id"]] = answer
        question_id++
      }    
    }
    mapped_questions["score"] = score
    console.log(mapped_questions)
    return mapped_questions
  }


  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(e)
    let data_to_db = map_question_answer(e.target)
    const sumPoints = sum(data_to_db)


    data_to_db["postal_code"] = document.querySelector('#code').value
    data_to_db["birth_month"] = document.querySelector('#month').value
    data_to_db["birth_year"] =  document.querySelector('#year').value


    console.log(data_to_db)
    //fetch POST
    if(data_to_db["score"] <=2){
      //pop up no issues 
      //<Modal isvisible />
      setShowModal(true)
      
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
        <Fragment>
        <div className=" flex items-center mb-4 space-x-3" >
        <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Kod pocztowy</label>
        <input type="number" id="code" name="code" className="inline-flex items-center "required />
        <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Miesiąc urodzenia</label>
        <input type="text" id="month" name="month" className="inline-flex items-center "required />
        <label className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Rok urodzenia</label>
        <input type="number" id="year" name="year" className="inline-flex items-center "required />
        </div>
          {questions["questions"].map(question => (
            <div key={question.id}>
              <a>
                <h3>{question.id}. {question.question_text_pl}</h3>
              </a>
          
          <div className=" flex items-center mb-4 space-x-3" >
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
          <Modal isVisible={showModal} score/>
          </Fragment>
        </form>
      </div>

    </main>
  );
};
  
export default base_form;