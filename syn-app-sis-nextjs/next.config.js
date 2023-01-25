/** @type {import('next').NextConfig} */
const nextConfig = {
  // redirects: async() =>{
  //   return[
  //     {
  //       source: "/",
  //       destination: "/base_form",
  //       permanent: true,
  //     }
  //   ]
  // },
  experimental: {
    appDir: true,
  },
}

module.exports = nextConfig
