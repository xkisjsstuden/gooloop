// firebase.js
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';

const firebaseConfig = {
    apiKey: "AIzaSyDQC7hZiF_l6hknHyDyG69myzEES89j054",
    authDomain: "goodloop-aeb99.firebaseapp.com",
    projectId: "goodloop-aeb99",
    storageBucket: "goodloop-aeb99.appspot.com",
    messagingSenderId: "71971149919",
    appId: "1:71971149919:web:810d64f496a2dee1ad63ea",
    measurementId: "G-JFGPX7BQWY"
  };

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const auth = getAuth(app);