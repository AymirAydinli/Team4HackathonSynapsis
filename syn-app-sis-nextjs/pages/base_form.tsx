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
    <main className="items-center justify-center content-center">
      <div>
        <h1>
        Wypełnij wszystkie pola
        </h1>

        {questions["questions"].map(question => (
          <div key={question.id} >
            <a>
              <h3>{question.id}. {question.pl}</h3>
            </a>
            <div>
          <input type="radio" value="Male" name={question.id} /> Tak
          <input type="radio" value="Female" name={question.id} /> Nie
        </div>
          </div>
        ))

        }

      </div>
    </main>
  );
};
  
export default base_form;