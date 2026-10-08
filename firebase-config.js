/**
 * LISHE KWA MTOTO — Firebase Config
 * ─────────────────────────────────────────────────────────────
 * 1. Go to: https://console.firebase.google.com/project/lishe-kwa-mtoto
 * 2. Project Settings → Your Apps → Web App
 * 3. Copy the firebaseConfig object values below
 * 4. In Firebase Console → Authentication → Sign-in method
 *    → Enable "Email/Password"
 * 5. Authentication → Users → Add user
 *    Email: admin@lishekwamtoto.org  Password: choose a strong one
 * 6. Firestore → Rules → paste these rules:
 *
 *    rules_version = '2';
 *    service cloud.firestore {
 *      match /databases/{database}/documents {
 *        // Public read for donations (donate page live feed)
 *        match /donations/{doc} {
 *          allow read: if true;
 *          allow write: if false; // only webhook server writes
 *        }
 *        // Everything else requires auth (admin dashboard)
 *        match /{document=**} {
 *          allow read, write: if request.auth != null;
 *        }
 *      }
 *    }
 * ─────────────────────────────────────────────────────────────
 */

const LISHE_FIREBASE_CONFIG = {
  apiKey: "AIzaSyCrqj8bvEQ8nLuJFxLClAGAvnGkaiYa7Hc",
  authDomain: "lishe-kwa-mtoto-c23a9.firebaseapp.com",
  projectId: "lishe-kwa-mtoto-c23a9",
  storageBucket: "lishe-kwa-mtoto-c23a9.firebasestorage.app",
  messagingSenderId: "1069234464410",
  appId: "1:1069234464410:web:b523840867314a3d5ae123"
};
