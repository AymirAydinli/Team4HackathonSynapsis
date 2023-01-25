import React from "react";
import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'

export const getStaticProps = async () =>{
  const resp = await fetch("http://127.0.0.1:8000/api/get_base_questions/")
  const data = await resp.json()

  return {
    props: {questions: data}
  }
}
   
const base_form = ({questions}) => {
  console.log(questions["q1"]["pl"]);

  return (
    <main>
    <div className="max-w-flex min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <h1>
      You are in the base form page 
      </h1>
      <p>{questions["q1"]["pl"]}</p>
    </div>
    </main>
  );
};
  
export default base_form;